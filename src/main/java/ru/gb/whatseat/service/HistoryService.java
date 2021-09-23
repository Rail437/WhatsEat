package ru.gb.whatseat.service;

import org.springframework.stereotype.Service;
import ru.gb.whatseat.entity.byUser.HistoryEntity;
import ru.gb.whatseat.entity.byUser.UserEntity;
import ru.gb.whatseat.repository.HistoryRepo;
import ru.gb.whatseat.repository.UserRepository;

import java.security.Principal;
import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;


@Service
public class HistoryService {
    private final HistoryRepo historyRepo;
    private final UserRepository userRepository;

    public HistoryService(HistoryRepo historyRepo, UserRepository userRepository) {
        this.historyRepo = historyRepo;
        this.userRepository = userRepository;
    }


    public void saveHistory(String[] str, Principal principal) {
        String result = convert(str);
        UserEntity user = userRepository.findByLogin(principal.getName());
        HistoryEntity history = new HistoryEntity(result, user);
        Locale local = new Locale("ru", "RU");
        DateFormat df = DateFormat.getDateTimeInstance(DateFormat.DEFAULT, DateFormat.DEFAULT, local);
        Date currentDate = new Date();
        System.out.println("currentDateTime = " + df.format(currentDate));
        history.setCreateData(df.format(currentDate));
        //System.out.println("То, что сохраняем в базе: " + history);
        historyRepo.save(history);
    }

    private String convert(String[] strings) {
        StringBuffer stringBuffer = new StringBuffer();
        for (int i = 0; i < strings.length; i++) {
            stringBuffer.append(strings[i]);
            stringBuffer.append(", ");
        }
        return stringBuffer.toString();
    }
}
