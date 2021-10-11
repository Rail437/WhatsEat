package ru.gb.whatseat.entity.byUser;

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


    public UserEntity() {
        this.favoriteDishEntities = new ArrayList<>();
        this.deferrerDishEntities = new ArrayList<>();
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
    @JoinTable(name = "users_favorites",
            joinColumns = @JoinColumn(name = "user_id"),
            inverseJoinColumns = @JoinColumn(name = "dish_id"))
    private Collection<DishEntity> favoriteDishEntities;


    @ManyToMany(fetch = FetchType.LAZY)
    @JoinTable(name = "users_deferrer",
            joinColumns = @JoinColumn(name = "user_id"),
            inverseJoinColumns = @JoinColumn(name = "dish_id"))
    private Collection<DishEntity> deferrerDishEntities;

    public void setFavoriteDishEntities(List<DishEntity> dishEntities) {
        this.favoriteDishEntities.addAll(dishEntities);
    }

    public void setDeferrerDishEntities(List<DishEntity> dishEntities) {
        this.deferrerDishEntities.addAll(dishEntities);
    }
    public void remuveFavorites(List<DishEntity> dishEntity){
        for (DishEntity entity : dishEntity) {
            this.favoriteDishEntities.remove(entity);
        }
    }
    public void remuveDeferrer(List<DishEntity> dishEntity){
        for (DishEntity entity : dishEntity) {
            this.deferrerDishEntities.remove(entity);
        }
    }
}
