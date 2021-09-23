package ru.gb.whatseat.service;


import ru.gb.whatseat.model.DishModel;
import ru.gb.whatseat.parametrs.ProductsList;

import java.security.Principal;
import java.util.List;

public interface DishService {
    List<DishModel> findAllByProduct(ProductsList productsList, Principal principal);
}
