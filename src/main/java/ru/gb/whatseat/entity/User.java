package ru.gb.whatseat.entity;

import lombok.Data;

import javax.persistence.*;
import java.util.Collection;
import java.util.UUID;

@Entity
@Data
@Table(name = "users")
public class User {
    @Id
    private UUID id;

    private String username;

    private String login;

    private String password;

    private String email;


    public User() {}

    public User(UUID id,String username) {
        this.id = id;
        this.username = username;
    }

    @ManyToMany
    @JoinTable(name = "users_roles",
            joinColumns = @JoinColumn(name = "user_id"),
            inverseJoinColumns = @JoinColumn(name = "role_id"))
    private Collection<Role> roles;

}
