package ru.gb.whatseat.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ru.gb.whatseat.model.UserDto;
import ru.gb.whatseat.service.UserService;

import java.security.Principal;

@RestController
@RequestMapping()
@RequiredArgsConstructor
public class UserController {
    @Autowired
    private UserService userService;

    @PostMapping("/registration")
    public ResponseEntity<HttpStatus> addUser(UserDto userDto) {
        return userService.saveUser(userDto)?
                new ResponseEntity<>(HttpStatus.CREATED):
                new ResponseEntity<>(HttpStatus.BAD_REQUEST);
    }

    @GetMapping("/client/test")
    public String test(Principal principal) {
        return principal.toString();
    }
}
