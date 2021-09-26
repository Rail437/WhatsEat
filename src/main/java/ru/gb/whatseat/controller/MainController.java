package ru.gb.whatseat.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import ru.gb.whatseat.parametrs.ProductsList;
import ru.gb.whatseat.service.DishService;

import java.security.Principal;

@Controller
@RequiredArgsConstructor
public class MainController {

    private final DishService dishService;

    @GetMapping
    public String listPage(Model model, ProductsList productsList, Principal principal){
        model.addAttribute("dishes", dishService.findAllByProduct(productsList,principal));
        return "index_new";
    }

    @GetMapping("/{id}")
    public String dishPage(@PathVariable("id") Long id, Model model, Principal principal){
        model.addAttribute("dish", dishService.findProductsByDishId(id, principal));
        return "dish_form";
    }

    /*@GetMapping(value = "/reg")
    public String reg(){
        return "registrate.html";
    }

    @GetMapping("/favorits")
    public String favorit(){
        return "favorite";
    }

    @GetMapping("/deferrer")
    public String def(){
        return "deferrer";
    }*/
}
