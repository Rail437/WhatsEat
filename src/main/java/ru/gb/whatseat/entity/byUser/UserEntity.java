package ru.gb.whatseat.entity.byUser;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;
import ru.gb.whatseat.entity.DishEntity;

import javax.persistence.*;
import java.util.*;

@Getter
@Setter
@Entity
@Table(name = "users")
public class UserEntity {
    @Id
    @Column(name = "user_id")
    private UUID id;

    private String username;

    private String login;

    private String password;

    private String email;


    public UserEntity() {}

    public UserEntity(UUID id, String username) {
        this.id = id;
        this.username = username;
    }

    @ManyToMany
    @JoinTable(name = "users_roles",
            joinColumns = @JoinColumn(name = "user_id"),
            inverseJoinColumns = @JoinColumn(name = "role_id"))
    private Collection<Role> roles;

    @OneToMany(mappedBy = "MyUser",fetch = FetchType.LAZY)
    private Set<HistoryEntity> histories = new HashSet<>();

    @OneToMany(mappedBy = "id",fetch = FetchType.LAZY)
    private Set<DishEntity> favorits = new HashSet<>();

    @ManyToMany(fetch = FetchType.LAZY)
    @JoinTable(name = "users_favorits",
            joinColumns = @JoinColumn(name = "user_id"),
            inverseJoinColumns = @JoinColumn(name = "dish_id"))
    private Collection<DishEntity> dishEntities;

    public void setDishEntities(List<DishEntity> dishEntities) {
        for (int i = 0; i < dishEntities.size() ; i++) {
            this.dishEntities.add(dishEntities.get(i));
        }
    }
}
