package org.example.service;

//import org.example.dao.Location;
import org.example.dao.User;
import org.example.repo.UserRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Set;
import java.util.stream.Collectors;

@Service
public class UserService {
    @Autowired
    UserRepo userRepo;

    public void addUser(User user) {
        userRepo.save(user);
    }

    public void deleteUserByUsername(String username) {
        userRepo.deleteById(username);
    }

    public Optional<User> getUserByUsername(String username) {
        return userRepo.findById(username);
    }

    public void updateUser(User user) {
        userRepo.save(user);
    }

    public boolean hasUser(String login) {
        return userRepo.findById(login).isPresent();
    }

    public List<User> getAll() {

        return ((List<User>) userRepo.findAll()).stream()
                .map(user -> new User(user.getLogin(), user.getLatitude(), user.getLongitude()))
                .collect(Collectors.toList());
    }

    public List<User> getFriends(String login) {
        ArrayList<User> u = (ArrayList<User>) userRepo.findAll();

        return  u.stream()
                .filter(user -> user.getFriends().stream()
                        .map(User::getLogin)
                        .toList()
                        .contains(login))
                .collect(Collectors.toList());
    }


//    public List<User> getFriends(String username) {
//        Optional<User> user =  userRepo.findById(username);
//        return user.map(User::getFriends).orElse(null);
//    }
//
//    public Location getLocation(String username) {
//        Optional<User> user = userRepo.findById(username);
//        return user.map(User::getLocation).orElse(null);
//    }
}