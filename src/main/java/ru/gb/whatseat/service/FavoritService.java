package ru.gb.whatseat.service;

import org.hibernate.mapping.Collection;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.gb.whatseat.entity.DishEntity;
import ru.gb.whatseat.entity.byUser.UserEntity;
import ru.gb.whatseat.model.DishModel;
import ru.gb.whatseat.repository.DishRepo;
import ru.gb.whatseat.repository.UserRepository;

import java.security.Principal;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

@Service
public class FavoritService {

    private final UserRepository userRepository;
    private final DishRepo dishRepo;

    @Autowired
    public FavoritService(UserRepository userRepository, DishRepo dishRepo) {
        this.userRepository = userRepository;
        this.dishRepo = dishRepo;
    }


    public boolean doFavorite(Principal principal, Long id) {
        if (principal != null & id != null) {
            UserEntity user = userRepository.findByLogin(principal.getName());
            List <DishEntity> dishEntity = dishRepo.findById(id).stream().collect(Collectors.toList());
            user.setDishEntities(dishEntity);
            userRepository.save(user);
            return true;
        }
        return false;
    }

    public List<DishModel> getFavorite(Principal principal) {
        UserEntity user = userRepository.findByLogin(principal.getName());
        List<DishModel> dishModels = user.getDishEntities().stream()
                .map(DishModel::toModel)
                .collect(Collectors.toList());
        return dishModels;
    }
}
