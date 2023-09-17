package org.example.controller;

import jakarta.annotation.Nullable;
import org.example.dao.User;
import org.example.repo.UserRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@RequestMapping(path="/user")
public class UserController {
    @Autowired
    UserRepo repo;

    @PostMapping(path="/add")
    public String addUser(@RequestParam String username,
                          @RequestParam String password,
                          @RequestParam @Nullable String email,
                          @RequestParam @Nullable String avatarURL) {
        repo.save(new User(username, password, avatarURL, email, null, null));
        return "saved";
    }

    @PostMapping(path="/delete")
    public String deleteUser(@RequestParam String username) {
        repo.deleteById(username);
        return "deleted";
    }
}
