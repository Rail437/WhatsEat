package ru.gb.whatseat.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Lazy;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import ru.gb.whatseat.model.byUserModels.UserDto;
import ru.gb.whatseat.entity.byUser.Role;
import ru.gb.whatseat.entity.byUser.UserEntity;
import ru.gb.whatseat.repository.HistoryRepo;
import ru.gb.whatseat.repository.RoleRepository;
import ru.gb.whatseat.repository.UserRepository;

import java.security.Principal;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
public class UserService implements UserDetailsService {

    private UserRepository userRepository;
    private final RoleRepository roleRepository;

    private PasswordEncoder bCryptPasswordEncoder;

    private HistoryRepo historyRepo;

    public UserService(RoleRepository roleRepository, HistoryRepo historyRepo) {
        this.roleRepository = roleRepository;
        this.historyRepo = historyRepo;
    }

    @Autowired
    public void setbCryptPasswordEncoder(@Lazy PasswordEncoder passwordEncoder) {
        this.bCryptPasswordEncoder = passwordEncoder;
    }

    @Autowired
    public void setUserRepository(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public UserEntity findByLogin(String login) {
        return userRepository.findByLogin(login);
    }

    @Override
    @Transactional
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        UserEntity user = findByLogin(username);
        if(user == null) {
            throw new UsernameNotFoundException(String.format("User '%s' not found", username));
        }
        return new org.springframework.security.core.userdetails.User(user.getUsername(), user.getPassword(),
                mapRolesToAuthorities(user.getRoles()));
    }

    private Collection<? extends GrantedAuthority> mapRolesToAuthorities(Collection<Role> roles) {
        return roles.stream().map(r -> new SimpleGrantedAuthority(r.getName())).collect(Collectors.toList());
    }

    public boolean saveUser(UserDto userDto) {
        UserEntity userFromDB = userRepository.findByLogin(userDto.getLogin());
        if (userFromDB != null) {
            return false;
        }
        saveRole();
        final UUID userId = UUID.randomUUID();
        UserEntity user = userDto.mapToUser();
        user.setId(userId);
        user.setRoles(Collections.singleton(new Role( 1L,"USER")));
        user.setPassword(bCryptPasswordEncoder.encode(user.getPassword()));
        userRepository.save(user);
        return true;
    }

    private void saveRole() {
        if (roleRepository.findByName("USER") == null) {
            roleRepository.save(new Role(1L, "USER"));
        }
        if (roleRepository.findByName("ADMIN") == null) {
            roleRepository.save(new Role(2L, "ADMIN"));
        }
    }

    public boolean deleteUser(UUID userId) {
        if (userRepository.findById(userId).isPresent()) {
            userRepository.deleteById(userId);
            return true;
        }
        return false;
    }

    public List<String> getHistory(Principal principal){
        UserEntity user = userRepository.findByLogin(principal.getName());
        return historyRepo.findByMyUser_Id(user.getId());
    }

    public boolean editUserPassword(UserDto userDto, Principal principal) {
        UserEntity userFromDB = userRepository.findByLogin(userDto.getLogin());
        if (userFromDB == null || principal.getName().equalsIgnoreCase(userFromDB.getLogin())) {
            return false;
        }
        userFromDB.setPassword(userDto.getPassword());
        userRepository.save(userFromDB);
        return true;
    }

    public UserDto getUserDto(Principal principal) {
        UserDto returnUserDto = UserDto.valueOf(userRepository.findByLogin(principal.getName()));
        returnUserDto.setPassword("Protected");
        return returnUserDto;
    }
}
