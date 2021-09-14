package ru.gb.whatseat.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import ru.gb.whatseat.parametrs.ProductsList;
import ru.gb.whatseat.service.DishService;

@Controller
@RequiredArgsConstructor
public class MainController {

    private final DishService dishService;

    @GetMapping
    public String listPage(Model model, ProductsList productsList){
        model.addAttribute("recipes", dishService.findAllByProduct(productsList));
        return "index_new";
    }

}
