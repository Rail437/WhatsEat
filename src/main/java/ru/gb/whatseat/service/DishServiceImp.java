package ru.gb.whatseat.service;

import org.springframework.data.jpa.domain.Specification;
import org.springframework.stereotype.Service;
import ru.gb.whatseat.entity.DishEntity;
import ru.gb.whatseat.model.DishModel;
import ru.gb.whatseat.parametrs.ProductsList;
import ru.gb.whatseat.repository.DishRepo;
import ru.gb.whatseat.repository.DishSpecification;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class DishServiceImp implements DishService{

    private  final DishRepo dishRepo;

    public DishServiceImp(DishRepo dishRepo) {
        this.dishRepo = dishRepo;
    }

    @Override
    public List<DishModel> findAllByProduct(ProductsList productsList) {

        Specification<DishEntity> spec = Specification.where(null);
        if(productsList.getProducts() != null){
            spec = spec.and(DishSpecification
                    .dishEntitySpecification(parsString(productsList.getProducts())));
        }

        return dishRepo.findAll(spec).stream()
                .map(dishEntity -> new DishModel(dishEntity.getId(),
                        dishEntity.getTitle(),
                        dishEntity.getDescription()))
                .collect(Collectors.toList());
    }

    private String[] parsString(String str){
        return str.split("\\s");
    }
}
