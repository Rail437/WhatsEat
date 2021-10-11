package ru.gb.whatseat.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import ru.gb.whatseat.model.DishModel;
import ru.gb.whatseat.service.FavoriteService;

import java.security.Principal;
import java.util.List;

@RestController
@RequestMapping("/api/v1")
public class FavoriteController {

    private final FavoriteService favoriteService;
    @Autowired
    public FavoriteController(FavoriteService favoriteService) {
        this.favoriteService = favoriteService;
    }

    @PostMapping("/doFavorite")
    public HttpStatus doFavorit(Principal principal,@RequestBody DishModel dishModel) {
        if (principal !=null & dishModel.getId() != null) {
            Long id = dishModel.getId();
            return favoriteService.doFavorite(principal,id)?
                    HttpStatus.OK :
                    HttpStatus.NOT_MODIFIED;
        }
        return HttpStatus.NOT_MODIFIED;
    }
    @GetMapping("/getFavorite")
    public List<DishModel> getFavorite(Principal principal) {
        if (principal != null) {
            return favoriteService.getFavorite(principal);
        }
        return null;
    }
    @PostMapping("/deleteFavorite")
    public HttpStatus deleteFavorite(Principal principal,@RequestBody DishModel dishModel) {
        if (principal !=null & dishModel.getId() != null) {
            Long id = dishModel.getId();
            return favoriteService.delFavorite(principal,id)?
                    HttpStatus.OK :
                    HttpStatus.NOT_MODIFIED;
        }
        return HttpStatus.NOT_MODIFIED;
    }



    @PostMapping("/doDeferrer")
    public HttpStatus doDeferrer(Principal principal,@RequestBody DishModel dishModel) {
        if (principal !=null & dishModel.getId() != null) {
            Long id = dishModel.getId();
            return favoriteService.doDeferrer(principal,id)?
                    HttpStatus.OK :
                    HttpStatus.NOT_MODIFIED;
        }
        return HttpStatus.NOT_MODIFIED;
    }
    @GetMapping("/getDeferrer")
    public List<DishModel> getDeferrer(Principal principal) {
        if (principal != null) {
            return favoriteService.getDeferrer(principal);
        }
        return null;
    }

    @PostMapping("/deleteDeferrer")
    public HttpStatus deleteDeferrer(Principal principal,@RequestBody DishModel dishModel) {
        if (principal !=null & dishModel.getId() != null) {
            Long id = dishModel.getId();
            return favoriteService.delDeferrer(principal,id)?
                    HttpStatus.OK :
                    HttpStatus.NOT_MODIFIED;
        }
        return HttpStatus.NOT_MODIFIED;
    }

}
