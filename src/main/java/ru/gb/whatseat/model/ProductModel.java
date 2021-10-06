package ru.gb.whatseat.model;

import lombok.Data;
import ru.gb.whatseat.entity.ProductEntity;
import ru.gb.whatseat.entity.RecipeEntity;

import java.util.List;
import java.util.stream.Collectors;

@Data
public class ProductModel {

    private  Long id;
    private String title;
    private List<RecipeModel> recipes;


    public ProductModel() {
    }

    public ProductModel(Long id, String title) {
        this.id = id;
        this.title = title;
    }

    public static ProductModel toModel(ProductEntity productEntity){
        ProductModel model = new ProductModel();
        model.setId(productEntity.getId());
        model.setTitle(productEntity.getTitle());
        model.setRecipes(productEntity.getRecipes().stream()
                .map(recipeEntity -> new RecipeModel(recipeEntity.getQuantity(),
                        ProductModel.toModel(recipeEntity.getProduct())))
                .collect(Collectors.toList()));
        return model;
    }
}
