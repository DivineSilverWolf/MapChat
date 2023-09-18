package org.example.controller;

import org.example.dao.Location;
import org.example.dao.User;
import org.example.repo.LocationRepo;
import org.example.repo.UserRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

@Controller
@RequestMapping("/user")
public class UserController {
    @Autowired
    UserRepo repo;

    @Autowired
    LocationRepo locationRepo;

    @PostMapping("/add")
    public String addUser(@RequestParam("username") String username,
                          @RequestParam("password") String password,
                          @RequestParam("email") String email,
                          @RequestParam("avatarURL") String avatarURL) {
        repo.save(new User(username, password, avatarURL, email, null, null, null));
        return "saved";
    }

    @PostMapping("/addLocation")
    public String addUser(@RequestParam("username") String username,
                          @RequestParam("latitude") Integer latitude,
                          @RequestParam("longitude") Integer longitude,
                          @RequestParam("timestamp") String timestamp) {

        DateFormat formatter = new SimpleDateFormat("yy:MM:dd:hh:mm:ss");
        Date date = null;

        try {
            date = formatter.parse(timestamp);
        } catch (ParseException e) {
            System.out.println("Invalid date");
        }

        var user = repo.findById(username);

        if (user.isEmpty()) {
            return "invalid user or location";
        }
        Location newlocation = new Location(latitude, longitude, date);

        locationRepo.save(newlocation);
        user.get().setLocation(newlocation);

        repo.save(user.get());

        return "saved";
    }

    @PostMapping("/delete")
    public String deleteUser(@RequestParam String username) {
        repo.deleteById(username);
        return "deleted";
    }
}
