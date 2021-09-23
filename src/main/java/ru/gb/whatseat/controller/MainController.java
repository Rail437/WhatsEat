package ru.gb.whatseat.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import ru.gb.whatseat.parametrs.ProductsList;
import ru.gb.whatseat.service.DishService;

import java.security.Principal;

@Controller
@RequiredArgsConstructor
public class MainController {

    private final DishService dishService;

    @GetMapping
    public String listPage(Model model, ProductsList productsList, Principal principal){
        model.addAttribute("recipes", dishService.findAllByProduct(productsList,principal));
        return "index_new";
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
