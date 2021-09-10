package ru.gb.whatseat.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ru.gb.whatseat.model.Client;
import ru.gb.whatseat.service.ClientService;

import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping(value = "/client")
public class ClientController {

    private final ClientService clientService;

    public ClientController(ClientService clientService) {
        this.clientService = clientService;
    }
    /**
     * Регистрация клиента. ПО средством POST запроса с передачей в JSON полей:
     * name,login,password.
     * @param client
     * @return
     */
    @PostMapping()
    public ResponseEntity<?> create(@RequestBody Client client) {
        System.out.println(client.toString());
        return clientService.create(client);
    }

    @GetMapping()
    public ResponseEntity<List<Client>> read() {
        final List<Client> clients = clientService.readAll();

        return clients != null &&  !clients.isEmpty()
                ? new ResponseEntity<>(clients, HttpStatus.OK)
                : new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }

    /**
     * Поиск клиента по UUID идентификатору
     * @param id
     * @return
     */
    @GetMapping(value = "/{id}")
    public ResponseEntity<Client> read(@PathVariable(name = "id") UUID id) {
        final Client client =  clientService.read(id).get();

        return client != null
                ? new ResponseEntity<>(client, HttpStatus.OK)
                : new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }

    /**
     *Обновление клиентов по UUID идентификатору
     * @param id
     * @param client
     * @return
     */
    @PutMapping(value = "/{id}")
    public ResponseEntity<?> update(@PathVariable(name = "id") UUID id, @RequestBody Client client) {
        final boolean updated = clientService.update(client, id);

        return updated
                ? new ResponseEntity<>(HttpStatus.OK)
                : new ResponseEntity<>(HttpStatus.NOT_MODIFIED);
    }

    /**
     * Удаление клиента по UUID идентификатору.
     * @param id
     * @return
     */
    @DeleteMapping(value = "/{id}")
    public ResponseEntity<?> delete(@PathVariable(name = "id") UUID id) {
        final boolean deleted = clientService.delete(id);

        return deleted
                ? new ResponseEntity<>(HttpStatus.OK)
                : new ResponseEntity<>(HttpStatus.NOT_MODIFIED);
    }
}
