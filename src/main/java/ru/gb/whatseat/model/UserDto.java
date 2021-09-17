package ru.gb.whatseat.model;

import lombok.Data;
import lombok.RequiredArgsConstructor;
import ru.gb.whatseat.entity.User;

import java.util.UUID;

@Data
@RequiredArgsConstructor
public class UserDto {
    private UUID id;
    private String name;
    private String login;
    private String password;
    private String Email;

    public UserDto(UUID id, String name, String login, String password, String mail) {
        this.id = id;
        this.name = name;
        this.login = login;
        this.password = password;
        this.Email = mail;
    }

    public static UserDto valueOf(User user) {
        return new UserDto(
                user.getId(),
                user.getUsername(),
                user.getLogin(),
                user.getPassword(),
                user.getEmail()
        );
    }

    public User mapToUser() {
        User user = new User();
        user.setId(id);
        user.setUsername(name);
        user.setLogin(login);
        user.setPassword(password);
        user.setEmail(Email);
        return user;
    }

    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }
}
