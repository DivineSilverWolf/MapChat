package org.example.controller;

import jakarta.annotation.Nullable;
import org.example.dao.Message;
import org.example.dao.User;
import org.example.repo.MessageRepo;
import org.example.repo.UserRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.sql.Time;
import java.util.Optional;

@Controller
@RequestMapping(path="/message")
public class MessageController {
    @Autowired
    UserRepo userRepo;

    @Autowired
    MessageRepo messageRepo;

    @PostMapping(path="/add")
    public String addMessage(@RequestParam String username,
                          @RequestParam String messageText,
                          @RequestParam Time timestamp) {

        Optional<User> user = userRepo.findById(username);
        if (user.isEmpty()) return "no such user";
        messageRepo.save(new Message(user.get(), messageText, timestamp));
        return "saved";
    }

    @PostMapping(path="/delete")
    public String deleteMessage(@RequestParam Long id) {
        messageRepo.deleteById(id);
        return "deleted";
    }
}
