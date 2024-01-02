package org.example.controller;

//import org.example.dao.Location;
import org.example.dao.User;
import org.example.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.lang.Nullable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;


import java.util.*;
import java.util.stream.Collectors;

@Controller
@RequestMapping("/")
public class UserController {
    @Autowired
    UserService userService;

    record UserInfo(String login, String password) {}
    record UserLocation(String login, @Nullable Double latitude, @Nullable Double longitude) {}
    record Password(String password) {}
    record Login(String login) {}

    @PostMapping("registration")
    public ResponseEntity<?> addNewUser(@RequestBody UserInfo user) {

        userService.addUser(new User(user.login, user.password));

        return new ResponseEntity<>(null, HttpStatus.OK);
    }

    @PostMapping("auth/{login}")
    public ResponseEntity<?> addReqisterUser(@PathVariable String login, @RequestBody Password password) {

        Optional<User> user = userService.getUserByUsername(login);

        if (user.isEmpty()) {
            return new ResponseEntity<>(null, HttpStatus.UNAUTHORIZED);
        }

        if (!Objects.equals(user.get().getPassword(), password.password)) {
            return new ResponseEntity<>(null, HttpStatus.NOT_ACCEPTABLE);
        }

        return new ResponseEntity<>(null, HttpStatus.OK);
    }

    @PostMapping("/location")
    public ResponseEntity<?> postLocationByLogin(@RequestBody UserLocation userLocation) {

        Optional<User> user = userService.getUserByUsername(userLocation.login);

        if (user.isEmpty()) {
            return new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
        }

        user.get().setLatitude(userLocation.latitude);
        user.get().setLongitude(userLocation.longitude);
        user.get().setTimestamp(new Date());

        userService.updateUser(user.get());

        return new ResponseEntity<>(null, HttpStatus.OK);
    }

    @GetMapping("/users")
    public ResponseEntity<List<User>> getAllUsers() {
        return new ResponseEntity<>(userService.getAll(), HttpStatus.OK);
    }

    @GetMapping("/location/{login}")
    public ResponseEntity<List<User>> getLocations(@PathVariable String login) {
        return new ResponseEntity<>(userService.getFriends(login).stream()
                .map(user-> new User(user.getLogin(), user.getLatitude(), user.getLongitude()))
                .collect(Collectors.toList()),
                HttpStatus.OK);
    }

    @PostMapping("/friends/add/{friendLogin}")
    public ResponseEntity<?> addFriend(@PathVariable("friendLogin") String friendLogin, @RequestBody Login login) {

        System.out.println(login);

        Optional<User> friend = userService.getUserByUsername(friendLogin);

        if (friend.isEmpty()) {
            return new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
        }

        Optional<User> user = userService.getUserByUsername(login.login);

        if (user.isEmpty()) {
            return new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
        }

        System.out.println(login + "отправил заявку" + friendLogin);

        friend.get().getFriendRequests().add(user.get());
        userService.updateUser(friend.get());

        if (user.get().getFriendRequests().contains(friend.get())) {
            return new ResponseEntity<>(new User(friend.get().getLogin(), friend.get().getLatitude(), friend.get().getLongitude()), HttpStatus.ACCEPTED);
        }

        return new ResponseEntity<>(new User(friend.get().getLogin(), friend.get().getLatitude(), friend.get().getLongitude()), HttpStatus.OK);
    }

    @GetMapping("/friends/confirm/{login}")
    public ResponseEntity<?> confirm(@PathVariable String login) {
        Optional<User> user = userService.getUserByUsername(login);

        if (user.isEmpty()) {
            return new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
        }

        System.out.println("User" + user.get().getLogin());

        List<User> friends = new ArrayList<>(user.get().getFriendRequests().stream()
                .filter(f -> f.getFriendRequests().contains(user.get()))
                .toList());

        System.out.println("Friends");
        friends.forEach(System.out::println);

        if (friends.isEmpty()) {
            System.out.println("Friends is empty");
            if (user.get().getFriendRequests().isEmpty()) {
                System.out.println("Friends requests is empty");
                return new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
            }
            System.out.println("Friends requests not empty");
            User u = user.get().getFriendRequests().get(0);

            return new ResponseEntity<>(
                    new User(u.getLogin(), u.getLatitude(), u.getLongitude()),
                    HttpStatus.ACCEPTED);
        }

        System.out.println("Friends not empty");

        User newFriend = friends.remove(0);

        user.get().getFriendRequests().remove(newFriend);
        user.get().getFriends().add(newFriend);
        userService.updateUser(user.get());

        newFriend.getFriendRequests().remove(user.get());
        newFriend.getFriends().add(user.get());
        userService.updateUser(newFriend);

        return new ResponseEntity<>(
                new User(newFriend.getLogin(), newFriend.getLatitude(), newFriend.getLongitude()),
                HttpStatus.OK);
    }
}