package ru.gb.whatseat.model;

import lombok.Data;
import ru.gb.whatseat.entity.DishEntity;

@Data
public class DishModel {

    private Long id;
    private String title;
    private String description;

    public DishModel() {
    }

    public DishModel(Long id, String title, String description) {
        this.id = id;
        this.title = title;
        this.description = description;
    }

    public static DishModel toModel(DishEntity dishEntity){
        DishModel model = new DishModel();
        model.setTitle(dishEntity.getTitle());
        model.setDescription(dishEntity.getDescription());
        return model;
    }
}
