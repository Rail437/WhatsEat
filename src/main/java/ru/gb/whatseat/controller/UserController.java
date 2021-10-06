package ru.gb.whatseat.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ru.gb.whatseat.model.byUserModels.UserDto;
import ru.gb.whatseat.service.UserService;

import java.security.Principal;
import java.util.List;

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

    @GetMapping("/api/v1/history")
    public List<String> testHistory(Principal principal) {
        if (principal != null) {
            return userService.getHistory(principal);
        }
        return null;
    }

    @PostMapping("/editpass")
    public ResponseEntity<HttpStatus> editPassword(UserDto userDto, Principal principal) {
        return userService.editUserPassword(userDto, principal)?
                new ResponseEntity<>(HttpStatus.OK):
                new ResponseEntity<>(HttpStatus.NOT_MODIFIED);
    }

}
