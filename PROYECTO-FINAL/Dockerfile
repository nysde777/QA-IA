# Use Jenkins LTS with Node.js support
FROM jenkins/jenkins:lts

# Switch to root user to install dependencies
USER root

# Install Node.js and npm
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

# Install dependencies for Cypress (GUI testing)
RUN apt-get update && apt-get install -y \
    libgtk2.0-0 \
    libgtk-3-0 \
    libgbm-dev \
    libnotify-dev \
    libgconf-2-4 \
    libnss3 \
    libxss1 \
    libasound2 \
    libxtst6 \
    xauth \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Create cypress cache directory
RUN mkdir -p /opt/cypress-cache
ENV CYPRESS_CACHE_FOLDER=/opt/cypress-cache

# Pre-install Cypress binary to avoid download during pipeline
RUN npm install -g cypress@14.5.2
RUN cypress install

# Switch back to jenkins user
USER jenkins

# Skip Jenkins setup wizard (optional - for automated setup)
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

# Copy Jenkins plugins list (we'll create this file next)
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt

# Install Jenkins plugins without strict version checking
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt || echo "Some plugins may have failed to install, continuing..."

# Expose Jenkins port
EXPOSE 8080

# The default CMD will start Jenkins
