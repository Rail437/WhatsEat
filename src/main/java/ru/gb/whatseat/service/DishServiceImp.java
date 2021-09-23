package ru.gb.whatseat.service;

import org.springframework.data.jpa.domain.Specification;
import org.springframework.stereotype.Service;
import ru.gb.whatseat.entity.DishEntity;
import ru.gb.whatseat.model.DishModel;
import ru.gb.whatseat.parametrs.ProductsList;
import ru.gb.whatseat.repository.DishRepo;
import ru.gb.whatseat.repository.DishSpecification;

import java.security.Principal;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class DishServiceImp implements DishService {
    private final HistoryService historyService;
    private final DishRepo dishRepo;

    public DishServiceImp(HistoryService historyService, DishRepo dishRepo) {
        this.historyService = historyService;
        this.dishRepo = dishRepo;
    }

    @Override
    public List<DishModel> findAllByProduct(ProductsList productsList, Principal principal) {

        Specification<DishEntity> spec = Specification.where(null);
        if (productsList.getProducts() != null) {
            String[] strings = parsString(productsList.getProducts());
            spec = spec.and(DishSpecification
                    .dishEntitySpecification(strings));
            if (principal != null) {
                historyService.saveHistory(strings, principal);
            }
        }

        return dishRepo.findAll(spec).stream()
                .map(dishEntity -> new DishModel(dishEntity.getId(),
                        dishEntity.getTitle(),
                        dishEntity.getDescription(),
                        dishEntity.getIngredients_list(),
                        dishEntity.getImg_path()))
                .collect(Collectors.toList());
    }

    private String[] parsString(String str) {
        return str.split("\\s");
    }


}
