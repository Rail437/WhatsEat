package ru.gb.whatseat.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.CrudRepository;
import ru.gb.whatseat.model.Client;

import java.util.UUID;

public interface ClientRepo extends CrudRepository<Client, UUID>, JpaRepository<Client, UUID> {
    Client findByLogin(String login);
    Client findByLoginAndPassword(String login, String password);
}
