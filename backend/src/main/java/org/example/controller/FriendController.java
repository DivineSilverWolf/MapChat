package org.example.controller;


import io.micrometer.common.lang.Nullable;
import org.example.dao.Chat;
import org.example.dao.Friend;
import org.example.dao.User;
import org.example.repo.FriendRepo;
import org.example.repo.UserRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@Controller
@RequestMapping(path="/friend")
public class FriendController {
    @Autowired
    FriendRepo friendRepo;
    @Autowired
    UserRepo userRepo;

    @PostMapping(path = "/add")
    public String addUser(@RequestParam String username,
                          @RequestParam String friendname) {

        var user =  userRepo.findById(username);
        var friend = userRepo.findById(friendname);
        if (user.isEmpty() || friend.isEmpty()) return "invalid id";

        friendRepo.save(new Friend(user.get(), friend.get()));
        return "saved";
    }

    @PostMapping(path = "/delete")
    public String deleteFriend(
            @RequestParam String username,
            @RequestParam String friendname) {
        return "not implemented";
    }
}