package org.example.controller;

import io.micrometer.common.lang.Nullable;
import org.example.dao.Chat;
import org.example.dao.User;
import org.example.repo.ChatRepo;
import org.example.repo.UserRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@RequestMapping(path="user")
public class ChatController {
    @Autowired
    ChatRepo repo;

    @Autowired
    UserRepo userRepo;

    @PostMapping(path="/add")
    public String addChat(@RequestParam String chatName,
                          @RequestParam @Nullable String chatType) {
//        Set<User> u = (Set<User>) userRepo.findAllById(users);

        repo.save(new Chat(chatName, chatType));
        return "saved";
    }

    @PostMapping(path="/delete")
    public String deleteChat(@RequestParam Long id) {
        repo.deleteById(id);
        return "deleted";
    }
}
