package ru.gb.whatseat.repository;

import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.Param;
import ru.gb.whatseat.entity.DishEntity;

import java.util.List;

public interface DishRepo extends CrudRepository<DishEntity, Long>, JpaSpecificationExecutor<DishEntity> {

    @Query("select d " +
            "from ProductEntity p " +
            "join fetch RecipeEntity r on (p.id=r.product) " +
            "join fetch DishEntity d on (r.dish=d.id) " +
            "where p.title in (:products) " +
            "group by r.dish ")
    List<DishEntity> findByProduct(@Param("products") String products);
}
