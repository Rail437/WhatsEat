package ru.gb.whatseat.model.byUserModels;

import lombok.Data;
import lombok.RequiredArgsConstructor;
import ru.gb.whatseat.entity.byUser.UserEntity;

import java.util.UUID;

@Data
@RequiredArgsConstructor
public class UserDto {
    private UUID id;
    private String username;
    private String login;
    private String password;
    private String Email;

    public UserDto(UUID id, String name, String login, String password, String mail) {
        this.id = id;
        this.username = name;
        this.login = login;
        this.password = password;
        this.Email = mail;
    }

    public static UserDto valueOf(UserEntity user) {
        return new UserDto(
                user.getId(),
                user.getUsername(),
                user.getLogin(),
                user.getPassword(),
                user.getEmail()
        );
    }

    public UserEntity mapToUser() {
        UserEntity user = new UserEntity();
        user.setId(id);
        user.setUsername(username);
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
