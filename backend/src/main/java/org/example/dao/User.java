package org.example.dao;


import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.validation.constraints.NotEmpty;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
public class User {
    @Id
    String username;
    String password;
    String avatarURL;
    String email;

    @ManyToOne
//    @JoinColumn(name = "location_id")
    Location location;

    @NotEmpty
    @ManyToMany(fetch = FetchType.LAZY)
    @JoinTable(name = "char_user",
            joinColumns = { @JoinColumn(name = "user_id") },
            inverseJoinColumns = { @JoinColumn(name = "chat_id") })

    Set<Chat> chats;

    public User(String username, String password, String avatarURL, String email, Location location, Set<Chat> chats) {
        this.username = username;
        this.password = password;
        this.avatarURL = avatarURL;
        this.email = email;
        this.location = location;
        this.chats = chats;
    }
}