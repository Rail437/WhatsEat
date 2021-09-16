package ru.gb.whatseat.repository;

import org.springframework.data.jpa.domain.Specification;
import ru.gb.whatseat.entity.DishEntity;
import ru.gb.whatseat.entity.ProductEntity;
import ru.gb.whatseat.entity.RecipeEntity;

import javax.persistence.criteria.*;
import java.util.ArrayList;
import java.util.List;

public final class DishSpecification {

    public static Specification<DishEntity> dishEntitySpecification(String[] productList){
        return (root, criteriaQuery, criteriaBuilder) -> {
            List<Predicate> predicates = new ArrayList<>();
            Join<DishEntity, RecipeEntity> recipes = root.join("recipes");
            Join<RecipeEntity, ProductEntity> products = recipes.join("product");
            for (String s : productList) {
                predicates.add(criteriaBuilder.equal(products.get("title"), s));
            }
            criteriaQuery.groupBy(root.get("id"));
            return criteriaBuilder.or(predicates.toArray(new Predicate[0]));
        };
    }
}
