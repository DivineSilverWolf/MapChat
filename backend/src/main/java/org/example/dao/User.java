package org.example.dao;


import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import javax.validation.constraints.NotEmpty;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Set;

@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
@Entity
public class User {
    @Id
    String login;
    String password;

    Double latitude;
    Double longitude;
    Date timestamp;

    @NotEmpty
    @ManyToMany(fetch = FetchType.LAZY)
    @JoinTable(name = "user_friend",
            joinColumns = { @JoinColumn(name = "user_id") },
            inverseJoinColumns = { @JoinColumn(name = "friend_id") }
    )
    List<User> friends;

    @NotEmpty
    @ManyToMany(fetch = FetchType.LAZY)
    @JoinTable(name = "Confirm",
            joinColumns = { @JoinColumn(name = "user1_id") },
            inverseJoinColumns = { @JoinColumn(name = "user2_id") }
    )
    List<User> friendRequests;

    public User(String login, String password) {
        this.login = login;
        this.password = password;
    }

    public User(String login, Double latitude, Double longitude) {
        this.login = login;
        this.latitude = latitude;
        this.longitude = longitude;
    }
}