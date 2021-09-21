package ru.gb.whatseat.model;

import lombok.Data;
import ru.gb.whatseat.entity.DishEntity;

@Data
public class DishModel {

    private Long id;
    private String title;
    private String description;
    private String ingredients_list;
    private String img_path;

    public DishModel() {
    }

    public DishModel(Long id, String title, String description) {
        this.id = id;
        this.title = title;
        this.description = description;
    }

    public DishModel(Long id, String title, String description, String ingredients_list, String img_path) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.ingredients_list = ingredients_list;
        this.img_path = img_path;
    }

    public static DishModel toModel(DishEntity dishEntity){
        DishModel model = new DishModel();
        model.setTitle(dishEntity.getTitle());
        model.setDescription(dishEntity.getDescription());
        model.setIngredients_list(dishEntity.getIngredients_list());
        model.setImg_path(dishEntity.getImg_path());
        return model;
    }
}
