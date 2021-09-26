package ru.gb.whatseat.model;

import lombok.Data;

@Data
public class RecipeModel {

    private String quantity;
    private ProductModel product;

    public RecipeModel(String quantity, ProductModel product) {
        this.quantity = quantity;
        this.product = product;
    }
}
