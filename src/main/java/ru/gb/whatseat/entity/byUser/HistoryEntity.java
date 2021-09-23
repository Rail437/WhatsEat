package ru.gb.whatseat.entity.byUser;


import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.CreatedDate;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Getter
@Setter
@Table(name = "user_history")
public class HistoryEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    private String createData;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "user_id")
    private UserEntity MyUser;

    public HistoryEntity() {
    }

    public HistoryEntity(String title, UserEntity user) {
        this.title = title;
        this.MyUser = user;
    }

    @Override
    public String toString() {
        return "HistoryEntity{" +
                "title='" + title + '\'' +
                ", createData=" + createData +
                ", MyUser=" + MyUser +
                '}';
    }
}
