package ru.gb.whatseat.repository;

import org.springframework.data.repository.CrudRepository;
import ru.gb.whatseat.entity.DishEntity;
import ru.gb.whatseat.entity.ProductEntity;
import ru.gb.whatseat.entity.RecipeEntity;

import java.util.List;

public interface RecipeRepo extends CrudRepository<RecipeEntity, Long> {

    List<RecipeEntity> findByProduct(ProductEntity product);
    RecipeEntity findByDish(DishEntity dish);
}
