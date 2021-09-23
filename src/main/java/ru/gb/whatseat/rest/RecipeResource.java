package ru.gb.whatseat.rest;

import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
import ru.gb.whatseat.model.DishModel;
import ru.gb.whatseat.parametrs.ProductsList;
import ru.gb.whatseat.service.DishService;

import java.security.Principal;
import java.util.List;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/v1")
public class RecipeResource {

    private final DishService dishService;

    @GetMapping(path = "/products", produces = "application/json")
    public List<DishModel> findByProduct(ProductsList productsList, Principal principal){
        return dishService.findAllByProduct(productsList, principal);
    }
}
