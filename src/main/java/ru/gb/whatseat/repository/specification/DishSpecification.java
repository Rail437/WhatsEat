package ru.gb.whatseat.repository.specification;

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
                Subquery<ProductEntity> subQuery = criteriaQuery.subquery(ProductEntity.class);
                subQuery.from(ProductEntity.class);
                subQuery.select(products.get("title"))
                        .where(criteriaBuilder.like(criteriaBuilder.lower(products.get("title")), s + "%"));
                predicates.add(criteriaBuilder.in(products.get("title")).value(subQuery));
            }
            criteriaQuery.groupBy(root.get("id"));
            return criteriaBuilder.or(predicates.toArray(new Predicate[0]));
        };
    }
}
