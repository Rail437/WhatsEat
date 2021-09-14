package ru.gb.whatseat.service;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import ru.gb.whatseat.model.Client;
import ru.gb.whatseat.repository.ClientRepo;

import java.util.List;
import java.util.UUID;
import java.util.concurrent.CopyOnWriteArrayList;

@Service
public class ClientService {

    private final ClientRepo clientRepo;
    private static List<Client> clients;

    public ClientService(ClientRepo clientRepo) {
        this.clientRepo = clientRepo;
        clients = new CopyOnWriteArrayList<Client>(clientRepo.findAll());
    }

    private void updateClientsList(Client client) {
        clients.add(client);
    }

    /**
     * Метод создание нового клиента и присваивания ему UUID.
     * @param client
     * @return
     */
    public ResponseEntity<?> create(Client client) {
        if (clientRepo.findByLogin(client.getLogin()) == null) {
            final UUID clientId = UUID.randomUUID();
            client.setClient_id(clientId);
            clientRepo.save(client);
            updateClientsList(client);
            return new ResponseEntity<>(HttpStatus.CREATED);
        }
        return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
    }

    /**
     * Метод проверки логина и пароля присланного клиентом.
     * @param client
     * @return
     */
    public Client findByLoginAndPass(Client client) {
        for (int i = 0; i < clients.size(); i++) {
            if (client.getLogin().equals(clients.get(i).getLogin()) && client.getPassword().equals(clients.get(i).getPassword())) {
                return clients.get(i);
            }
        }
        return null; // Чтобы не обращаться каждый раз в БД.
    }

    public Client read(UUID id) {
        //return CLIENT_UUID_REPOSITORY_MAP.get(id);
        for (int i = 0; i < clients.size(); i++) {
            if (clients.get(i).getClient_id() == id) {
                return clients.get(i);
            }
        }
        return null;
    }

    /**
     * Метод изменения полей клиента. Но здесь важно прислать в теле JSON и UUID клиента которого меняем.
     * @param client
     * @return
     */
    public boolean update(Client client) {
        for (int i = 0; i < clients.size(); i++) {
            if (client.getClient_id().equals(clients.get(i).getClient_id())) {
                clientRepo.save(client);
                clients.remove(i);
                clients.add(client);
                return true;
            }
        }
        return false;
    }

    /**
     * Метод удаления клиента по его UUID
     * @param id
     * @return
     */
    public boolean delete(UUID id, Client client) {
        if (client.getClient_id().equals(id)) {
            for (int i = 0; i < clients.size(); i++) {
                if (clients.get(i).getClient_id() == id) {
                    clientRepo.deleteById(id);
                    clients.remove(i);
                    return true;
                }
            }
        }
        return false;
    }
}
