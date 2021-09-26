package ru.gb.whatseat.repository;

import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.Param;
import ru.gb.whatseat.entity.DishEntity;

import java.util.List;

public interface DishRepo extends CrudRepository<DishEntity, Long>, JpaSpecificationExecutor<DishEntity> {

    @Query("select d " +
            "from DishEntity d " +
            "join fetch RecipeEntity r on(r.dish=d.id) " +
            "join fetch ProductEntity p on(r.product=p.id) " +
            "where d.id = :id")
    DishEntity findByDishId(@Param("id") Long id);
}
