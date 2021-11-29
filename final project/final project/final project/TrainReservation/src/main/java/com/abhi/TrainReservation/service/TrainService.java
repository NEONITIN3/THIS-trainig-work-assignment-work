package com.abhi.TrainReservation.service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.abhi.TrainReservation.model.Train;
import com.abhi.TrainReservation.repository.TrainRepository;

@Service
public class TrainService {

	private final TrainRepository trainRepository;

	@Autowired
	public TrainService(TrainRepository trainRepository) {

		this.trainRepository = trainRepository;

		Train train1 = new Train(12961, "Avantika Express", "Mumbai", "Indore", 530.0);

		Train train2 = new Train(22691, "Rajdhani Express", "Bengaluru", "Delhi", 1200.0);

		Train train3 = new Train(12302, "Howrah Express", "Howrah", "Delhi", 850.0);

		Train train4 = new Train(16128, "Chennai Express", "Mumbai", "chennai", 1500.0);	
		
		Train train5 = new Train(12989, "Ajmer SF Special", "Dadar", "Ajmer", 760.0);
		
		Train train6 = new Train(82901, "Tejas Express", "Mumbai", "Ahemdabad", 1500.0);
		
		Train train7 = new Train(20903, "Mahamana Express", "Varanasi", "Surat", 1250.0);

		Train train8 = new Train(22436, "Vande Bharat Express", "Delhi", "Prayagraj", 580.0);
		
		List<Train> trains = new ArrayList<Train>();
		trains.add(train1);
		trains.add(train2);
		trains.add(train3);
		trains.add(train4);
		trains.add(train5);
		trains.add(train6);
		trains.add(train7);
		trains.add(train8);

		trainRepository.saveAll(trains);
	}

	public Optional<Train> getTrainByNumber(int trainNumber) {
		return trainRepository.findById(trainNumber);
	}

	public List<Train> getAllTrains() {
		return trainRepository.findAll();
	}

	

}