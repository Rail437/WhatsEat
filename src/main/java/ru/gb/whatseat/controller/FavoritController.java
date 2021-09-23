package ru.gb.whatseat.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ru.gb.whatseat.model.DishModel;
import ru.gb.whatseat.model.MyLong;
import ru.gb.whatseat.service.FavoritService;

import java.security.Principal;
import java.util.List;

@RestController
@RequestMapping("/api/v1")
public class FavoritController {

    private final FavoritService favoritService;
    @Autowired
    public FavoritController(FavoritService favoritService) {
        this.favoritService = favoritService;
    }

    @PostMapping("/doFavorit")
    public HttpStatus doFavorit(Principal principal, DishModel dishModel) {
        if (principal !=null & dishModel.getId() != null) {
            Long id = dishModel.getId();
            return favoritService.doFavorite(principal,id)?
                    HttpStatus.OK :
                    HttpStatus.NOT_MODIFIED;
        }
        return HttpStatus.NOT_MODIFIED;
    }
    @GetMapping("/getFavorit")
    public List<DishModel> getFavorit(Principal principal) {
        if (principal != null) {
            return favoritService.getFavorite(principal);
        }
        return null;
    }

}
