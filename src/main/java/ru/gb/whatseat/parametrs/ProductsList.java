package ru.gb.whatseat.parametrs;


import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;

@Data
@Builder
@AllArgsConstructor
public class ProductsList {
    private String products;
}
