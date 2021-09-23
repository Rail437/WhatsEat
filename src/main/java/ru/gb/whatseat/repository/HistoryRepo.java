package ru.gb.whatseat.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import ru.gb.whatseat.entity.byUser.HistoryEntity;

import java.util.List;
import java.util.UUID;

public interface HistoryRepo extends JpaRepository<HistoryEntity, Long> {
    @Query(value = "select title from user_history WHERE user_id = :uuid", nativeQuery = true)
    List<String> findByMyUser_Id(@Param("uuid") UUID uuid);
}
