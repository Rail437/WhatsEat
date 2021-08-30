package ru.gb.whatseat.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import ru.gb.whatseat.entity.RecipeEntity;
import ru.gb.whatseat.model.ProductsList;
import ru.gb.whatseat.repository.ProductRepo;
import ru.gb.whatseat.repository.RecipeRepo;
import ru.gb.whatseat.service.DishService;


import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

@Controller
@RequiredArgsConstructor
public class MainController {

    private final DishService dishService;
    private final RecipeRepo recipeRepo;
    private final ProductRepo productRepo;

    @GetMapping
    public String listPage(Model model, @RequestParam("products") Optional<String> products){

        List<RecipeEntity> recipes;
        if(products.isPresent()){
            recipes = recipeRepo.findByProduct(productRepo.findByTitle(products.get()));
        } else {
            recipes = StreamSupport.stream(recipeRepo.findAll().spliterator(),false)
                    .collect(Collectors.toList());
        }
        model.addAttribute("recipes", recipes);
        return "index_new";
    }

//    @GetMapping
//    public String first(Model model){
//        model.addAttribute("dish", dishService.getDish());
//        return "index";
//    }

    @PostMapping("/")
    public String inProducts(@ModelAttribute ProductsList productsList){
        dishService.findDish(productsList);
        return "redirect:/";
    }
}
