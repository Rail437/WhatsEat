package ru.gb.whatseat.service;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import ru.gb.whatseat.model.Client;
import ru.gb.whatseat.repository.ClientRepo;

import java.util.*;

@Service
public class ClientService{

    private final ClientRepo clientRepo;

    public ClientService(ClientRepo clientRepo) {
        this.clientRepo = clientRepo;
    }

    public ResponseEntity<?> create(Client client) {
        if (clientRepo.findByLogin(client.getLogin()) == null) {
            final UUID clientId = UUID.randomUUID();
            client.setClient_id(clientId);
            clientRepo.save(client);
            return new ResponseEntity<>(HttpStatus.CREATED);
        }
        return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
    }

    public Client findByLoginAndPass(Client client) {
        //return new ArrayList<>(CLIENT_UUID_REPOSITORY_MAP.values());
        return clientRepo.findByLoginAndPassword(client.getLogin(),client.getPassword());
    }

    public Optional<Client> read(UUID id) {
        //return CLIENT_UUID_REPOSITORY_MAP.get(id);
        return clientRepo.findById(id);
    }

    public boolean update(Client client, UUID id) {
        if (clientRepo.findById(id).isPresent()) { //надо придумать, как обезопасить изменения от злоумышленников
            clientRepo.findById(id).get().setName(client.getName());
            clientRepo.findById(id).get().setLogin(client.getLogin());
            clientRepo.findById(id).get().setPassword(client.getPassword());
            clientRepo.flush();
            return true;
        }
        return false;
    }

    public boolean delete(UUID id) {
        if (clientRepo.findById(id).isPresent()) {
            clientRepo.deleteById(id);
            return true;
        }
        return false;
    }
}
