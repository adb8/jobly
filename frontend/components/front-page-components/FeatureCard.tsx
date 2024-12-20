import React from "react";
import { Container, Grid, Box, Typography, Paper } from "@mui/material";
import { FaChartArea } from "react-icons/fa";

const FeatureCard = ({
  feature,
}: {
  feature: {
    title: string;
    description: string;
  };
}) => {
  return (
    <Grid item xs={12} sm={6} md={4}>
      <Paper
        elevation={2}
        sx={{
          padding: "50px",
          borderRadius: "15px",
        }}>
        <FaChartArea color="black" size="2.5rem" />
        <Typography
          variant="h6"
          mb={1}
          mt={4}
          sx={{
            color: "black",
            fontWeight: "bold",
            fontSize: "1.3rem",
          }}>
          {feature.title}
        </Typography>
        <Typography
          variant="body1"
          sx={{ color: "black", fontSize: "1.1rem", fontWeight: "regular" }}>
          {feature.description}
        </Typography>
        <Box mt={2}>
          <a href="#" style={{ color: "blue", textDecoration: "none", fontWeight: "bold", fontSize: "1.1rem" }}>
            Learn More
          </a>
        </Box>
      </Paper>
    </Grid>
  );
};

export default FeatureCard;
