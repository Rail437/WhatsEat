package ru.gb.whatseat.model.byUserModels;

import lombok.Data;
import lombok.RequiredArgsConstructor;
import ru.gb.whatseat.entity.byUser.HistoryEntity;
import ru.gb.whatseat.entity.byUser.UserEntity;

@Data
@RequiredArgsConstructor
public class HistoryDto {
    private String title;
    private UserEntity userEntity;

    public HistoryDto(String title, UserEntity user) {
        this.title = title;
        this.userEntity = user;
    }

    public static HistoryDto valueOf(HistoryEntity history) {
        return new HistoryDto(
                history.getTitle(),
                history.getMyUser()
        );
    }

    public HistoryEntity mapToHistoryEntity() {
        HistoryEntity history = new HistoryEntity();
        history.setTitle(title);
        history.setMyUser(userEntity);
        return history;
    }
}
