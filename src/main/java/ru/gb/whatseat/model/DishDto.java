package ru.gb.whatseat.model;

import lombok.Data;

import java.util.List;
import java.util.stream.Collectors;

@Data
public class DishDto {

    private Long id;
    private String title;
    private String description;
    private String img;
    private List<RecipeModel> recipes;

    public DishDto(DishModel dishModel) {
        this.id = dishModel.getId();
        this.title = dishModel.getTitle();
        this.description = dishModel.getDescription();
        this.img = dishModel.getImg_path();
        this.recipes = dishModel.getRecipe().stream()
                .map(recipeEntity -> new RecipeModel(recipeEntity.getQuantity(),
                        new ProductModel(recipeEntity.getProduct().getId(),recipeEntity.getProduct().getTitle())
                )).collect(Collectors.toList());
    }
}
