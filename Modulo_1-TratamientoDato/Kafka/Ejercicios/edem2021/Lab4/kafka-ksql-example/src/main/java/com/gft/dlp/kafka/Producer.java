package com.gft.dlp.kafka;

import com.github.javafaker.Faker;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.text.NumberFormat;
import java.util.Locale;
import java.util.Properties;
import java.util.UUID;
import java.util.concurrent.TimeUnit;

public class Producer {

    public static void main(String[] args){
        Properties properties = new Properties();
        properties.put("bootstrap.servers", "localhost:9092");
        properties.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        properties.put("value.serializer", "com.gft.dlp.kafka.OrderJsonSerializer");

        KafkaProducer<String, Order> kafkaProducer = new KafkaProducer<String, Order>(properties);
        Faker faker = new Faker();
        try{
            NumberFormat format = NumberFormat.getInstance(Locale.FRENCH);
             for(int i = 0; i < 1000; i++){

                Order order = new Order (UUID.randomUUID().toString(),
                        faker.number().numberBetween(1,5),
                        faker.commerce().productName(),
                        faker.number().numberBetween(1,100),
                        format.parse(faker.commerce().price()).doubleValue(),
                        faker.date().past(10, TimeUnit.DAYS));
                System.out.println(order);
                kafkaProducer.send(new ProducerRecord<String, Order>("orders", order.getOrderId(), order ));
            }
        }catch (Exception e){
            e.printStackTrace();
        }finally {
            kafkaProducer.close();
        }
    }
}
