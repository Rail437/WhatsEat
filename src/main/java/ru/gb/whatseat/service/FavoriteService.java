package ru.gb.whatseat.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.gb.whatseat.entity.DishEntity;
import ru.gb.whatseat.entity.byUser.UserEntity;
import ru.gb.whatseat.model.DishDto;
import ru.gb.whatseat.model.DishModel;
import ru.gb.whatseat.repository.DishRepo;
import ru.gb.whatseat.repository.UserRepository;

import java.security.Principal;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class FavoriteService {

    private final UserRepository userRepository;
    private final DishRepo dishRepo;

    @Autowired
    public FavoriteService(UserRepository userRepository, DishRepo dishRepo) {
        this.userRepository = userRepository;
        this.dishRepo = dishRepo;
    }


    public boolean doFavorite(Principal principal, Long id) {
        if (principal != null & id != null) {
            UserEntity user = userRepository.findByLogin(principal.getName());
            List <DishEntity> dishEntity = dishRepo.findById(id).stream().collect(Collectors.toList());
            user.setFavoriteDishEntities(dishEntity);
            userRepository.save(user);
            return true;
        }
        return false;
    }

    public List<DishModel> getFavorite(Principal principal) {
        UserEntity user = userRepository.findByLogin(principal.getName());
        return user.getFavoriteDishEntities().stream()
                .map(dishEntity -> new DishModel(dishEntity.getId(),
                        dishEntity.getTitle(),
                        dishEntity.getDescription(),
                        dishEntity.getIngredients_list(),
                        dishEntity.getImg_path())   )
                .collect(Collectors.toList());
    }

    public boolean delFavorite(Principal principal, Long id) {
        if (principal != null & id != null) {
            UserEntity user = userRepository.findByLogin(principal.getName());
            List <DishEntity> dishEntity = dishRepo.findById(id).stream().collect(Collectors.toList());
            user.remuveFavorites(dishEntity);
            userRepository.save(user);
            return true;
        }
        return false;
    }

    public boolean doDeferrer(Principal principal, Long id) {
        if (principal != null & id != null) {
            UserEntity user = userRepository.findByLogin(principal.getName());
            List <DishEntity> dishEntity = dishRepo.findById(id).stream().collect(Collectors.toList());
            user.setDeferrerDishEntities(dishEntity);
            userRepository.save(user);
            return true;
        }
        return false;
    }

    public List<DishModel> getDeferrer(Principal principal) {
        UserEntity user = userRepository.findByLogin(principal.getName());
        return user.getDeferrerDishEntities().stream()
                .map(DishModel::toModel)
                .collect(Collectors.toList());
    }

    public boolean delDeferrer(Principal principal, Long id) {
        if (principal != null & id != null) {
            UserEntity user = userRepository.findByLogin(principal.getName());
            List <DishEntity> dishEntity = dishRepo.findById(id).stream().collect(Collectors.toList());
            user.remuveDeferrer(dishEntity);
            userRepository.save(user);
            return true;
        }
        return false;
    }
}
