package ru.gb.whatseat.entity;


import lombok.Data;

import javax.persistence.*;
import java.util.List;

@Data
@Entity
@Table(name = "dish_entity")
public class DishEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    private int diffLevel;
    private String description;

    @ManyToOne
    @JoinColumn(name = "category_id")
    private DishCategoryEntity dish_category;

    @OneToMany(mappedBy = "dish")
    private List<RecipeEntity> recipes;
}
