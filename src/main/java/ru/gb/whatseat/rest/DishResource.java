package ru.gb.whatseat.rest;

import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
import ru.gb.whatseat.model.DishDto;
import ru.gb.whatseat.model.DishModel;
import ru.gb.whatseat.parametrs.ProductsList;
import ru.gb.whatseat.service.DishService;

import java.security.Principal;
import java.util.List;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/v1")
public class DishResource {

    private final DishService dishService;

    @GetMapping(path = "/dishes", produces = "application/json")
    public List<DishModel> findByProduct(ProductsList productsList, Principal principal){
        return dishService.findAllByProduct(productsList, principal);
    }

    @GetMapping("/dishes/{id}")
    public DishDto dishPage(@PathVariable("id") Long id, Principal principal){
        return dishService.findProductsByDishId(id, principal);
    }
}
