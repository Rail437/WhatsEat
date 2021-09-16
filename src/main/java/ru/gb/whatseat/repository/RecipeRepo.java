package ru.gb.whatseat.repository;

import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.Param;
import ru.gb.whatseat.entity.DishEntity;
import ru.gb.whatseat.entity.ProductEntity;
import ru.gb.whatseat.entity.RecipeEntity;

import java.util.List;

public interface RecipeRepo extends CrudRepository<RecipeEntity, Long>, JpaSpecificationExecutor<RecipeEntity> {

    List<RecipeEntity> findDistinctByProduct(ProductEntity product);

    RecipeEntity findByDish(DishEntity dish);

    @Query("select d.title " +
            "from ProductEntity p " +
            "join fetch RecipeEntity r on (p.id = r.product) " +
            "join fetch DishEntity d on (r.dish = d.id) " +
            "where p.title= :products")
    List<String> findByProduct(@Param("products") String products);


}
